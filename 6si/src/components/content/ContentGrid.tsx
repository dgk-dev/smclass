"use client";

import { useEffect, useRef, useCallback } from 'react';
import { Content } from '@/types';
import { ContentCard } from './ContentCard';
import { useInfiniteScroll } from '@/hooks/useInfiniteScroll';
import { useAuth } from '@/contexts/auth';
import { createClient } from '@/lib/supabase/client';
import { useRouter } from 'next/navigation';

interface ContentGridProps {
  category?: 'news' | 'community' | 'deals';
}

export function ContentGrid({ category }: ContentGridProps) {
  const { items, loading, error, hasMore, loadMore } = useInfiniteScroll({ category });
  const { user } = useAuth();
  const router = useRouter();
  const supabase = createClient();
  const observer = useRef<IntersectionObserver>();
  
  const lastElementRef = useCallback((node: HTMLDivElement) => {
    if (loading) return;
    
    if (observer.current) {
      observer.current.disconnect();
    }
    
    observer.current = new IntersectionObserver(entries => {
      if (entries[0].isIntersecting && hasMore) {
        loadMore();
      }
    });
    
    if (node) {
      observer.current.observe(node);
    }
  }, [loading, hasMore, loadMore]);

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

    const { data: existingLike } = await supabase
      .from('user_interactions')
      .select()
      .eq('user_id', user.id)
      .eq('content_id', contentId)
      .eq('type', 'like')
      .single();

    if (existingLike) {
      await supabase
        .from('user_interactions')
        .delete()
        .eq('user_id', user.id)
        .eq('content_id', contentId)
        .eq('type', 'like');
    } else {
      await supabase
        .from('user_interactions')
        .insert({
          user_id: user.id,
          content_id: contentId,
          type: 'like'
        });
    }
    
    router.refresh();
  }, [user, router, supabase]);

  const handleBookmark = useCallback(async (contentId: string) => {
    if (!user) {
      router.push('/auth/login');
      return;
    }

    const { data: existingBookmark } = await supabase
      .from('user_interactions')
      .select()
      .eq('user_id', user.id)
      .eq('content_id', contentId)
      .eq('type', 'bookmark')
      .single();

    if (existingBookmark) {
      await supabase
        .from('user_interactions')
        .delete()
        .eq('user_id', user.id)
        .eq('content_id', contentId)
        .eq('type', 'bookmark');
    } else {
      await supabase
        .from('user_interactions')
        .insert({
          user_id: user.id,
          content_id: contentId,
          type: 'bookmark'
        });
    }
    
    router.refresh();
  }, [user, router, supabase]);

  const handleClick = useCallback((url: string) => {
    window.open(url, '_blank');
  }, []);

  if (error) {
    return <div className="text-red-500">Error: {error}</div>;
  }

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 p-4">
      {items.map((item, index) => (
        <div
          key={item.id}
          ref={index === items.length - 1 ? lastElementRef : undefined}
        >
          <ContentCard
            {...item}
            isNew={isNew(item.timestamp)}
            isLiked={false} // TODO: Implement user interaction state
            isBookmarked={false} // TODO: Implement user interaction state
            onLike={() => handleLike(item.id)}
            onBookmark={() => handleBookmark(item.id)}
            onClick={() => handleClick(item.url)}
          />
        </div>
      ))}
      {loading && (
        <div className="col-span-full text-center py-4">
          Loading...
        </div>
      )}
    </div>
  );
}
