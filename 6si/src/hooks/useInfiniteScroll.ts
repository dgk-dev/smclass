'use client';

import { useEffect, useState } from 'react';
import { Content } from '@/types';
import { createClient } from '@/lib/supabase/client';

interface UseInfiniteScrollProps {
  category?: 'news' | 'community' | 'deals';
  limit?: number;
}

export function useInfiniteScroll({ category, limit = 10 }: UseInfiniteScrollProps = {}) {
  const [items, setItems] = useState<Content[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [hasMore, setHasMore] = useState(true);
  const [page, setPage] = useState(0);
  
  const supabase = createClient();

  const loadMore = async () => {
    if (loading || !hasMore) return;

    setLoading(true);
    try {
      let query = supabase
        .from('contents')
        .select('*')
        .order('timestamp', { ascending: false })
        .range(page * limit, (page + 1) * limit - 1);

      if (category) {
        query = query.eq('category', category);
      }

      const { data, error } = await query;

      if (error) throw error;

      if (data) {
        // Deduplicate items based on id
        const newItems = data.filter(
          newItem => !items.some(existingItem => existingItem.id === newItem.id)
        );
        
        if (newItems.length > 0) {
          setItems(prev => [...prev, ...newItems]);
          setHasMore(data.length === limit);
          setPage(prev => prev + 1);
        } else {
          setHasMore(false);
        }
      }
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadMore();
  }, []); // Initial load

  return {
    items,
    loading,
    error,
    hasMore,
    loadMore
  };
}
