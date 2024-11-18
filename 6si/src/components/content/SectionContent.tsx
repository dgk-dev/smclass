"use client";

import { useCallback, useEffect, useState } from 'react';
import { Content } from '@/types';
import { ContentCard } from './ContentCard';
import { useAuth } from '@/contexts/auth';
import { createClient } from '@/lib/supabase/client';
import { useRouter } from 'next/navigation';

interface SectionContentProps {
  category: 'news' | 'community' | 'deals';
  limit?: number;
}

export function SectionContent({ category, limit = 10 }: SectionContentProps) {
  const [items, setItems] = useState<Content[]>([]);
  const [loading, setLoading] = useState(true);
  const { user } = useAuth();
  const router = useRouter();
  const supabase = createClient();

  useEffect(() => {
    const fetchItems = async () => {
      try {
        const { data, error } = await supabase
          .from('contents')
          .select('*')
          .eq('category', category)
          .order('timestamp', { ascending: false })
          .limit(limit);

        if (error) throw error;
        setItems(data || []);
      } catch (error) {
        console.error('Error fetching items:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchItems();
  }, [category, limit, supabase]);

  const isNew = useCallback((timestamp: string) => {
    const date = new Date(timestamp);
    const sixHoursAgo = new Date(Date.now() - 6 * 60 * 60 * 1000);
    return date > sixHoursAgo;
  }, []);

  const handleLike = useCallback(async (contentId: string) => {
    if (!user) {
      router.push('/auth/login');
      return;
    }

    try {
      const { data: likes } = await supabase
        .from('user_likes')
        .select('content_id')
        .eq('user_id', user.id)
        .eq('content_id', contentId);

      if (!likes?.length) {
        await supabase
          .from('user_likes')
          .insert({ user_id: user.id, content_id: contentId });
      } else {
        await supabase
          .from('user_likes')
          .delete()
          .eq('user_id', user.id)
          .eq('content_id', contentId);
      }
    } catch (error) {
      console.error('Error handling like:', error);
    }
  }, [user, router, supabase]);

  const handleBookmark = useCallback(async (contentId: string) => {
    if (!user) {
      router.push('/auth/login');
      return;
    }

    try {
      const { data: bookmarks } = await supabase
        .from('user_bookmarks')
        .select('content_id')
        .eq('user_id', user.id)
        .eq('content_id', contentId);

      if (!bookmarks?.length) {
        await supabase
          .from('user_bookmarks')
          .insert({ user_id: user.id, content_id: contentId });
      } else {
        await supabase
          .from('user_bookmarks')
          .delete()
          .eq('user_id', user.id)
          .eq('content_id', contentId);
      }
    } catch (error) {
      console.error('Error handling bookmark:', error);
    }
  }, [user, router, supabase]);

  if (loading) {
    return <div className="animate-pulse">Loading...</div>;
  }

  return (
    <div className="flex flex-col divide-y divide-gray-100">
      {items.map((item) => (
        <ContentCard
          key={item.id}
          {...item}
          isNew={isNew(item.timestamp)}
          isLiked={user?.likes?.includes(item.id)}
          isBookmarked={user?.bookmarks?.includes(item.id)}
          onLike={() => handleLike(item.id)}
          onBookmark={() => handleBookmark(item.id)}
        />
      ))}
    </div>
  );
}
