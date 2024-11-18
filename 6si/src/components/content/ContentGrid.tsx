"use client";

import { useEffect, useRef, useCallback } from 'react';
import { Content } from '@/types';
import { ContentCard } from './ContentCard';
import { useInfiniteScroll } from '@/hooks/useInfiniteScroll';

interface ContentGridProps {
  category?: 'news' | 'community' | 'deals';
}

export function ContentGrid({ category }: ContentGridProps) {
  const { items, loading, error, hasMore, loadMore } = useInfiniteScroll({ category });
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
