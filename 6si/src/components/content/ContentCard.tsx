"use client";

import { ContentCardProps } from '@/types';
import Image from 'next/image';
import { format, formatDistanceToNow } from 'date-fns';
import { ko } from 'date-fns/locale';
import { useMemo } from 'react';
import { Heart, Bookmark } from 'lucide-react';

export function ContentCard({
  thumbnail,
  title,
  source,
  timestamp,
  isNew,
  category,
  url,
  likes = 0,
  bookmarks = 0,
  isLiked = false,
  isBookmarked = false,
  onLike,
  onBookmark,
  onClick
}: ContentCardProps) {
  const date = useMemo(() => new Date(timestamp), [timestamp]);
  const timeAgo = useMemo(
    () => formatDistanceToNow(date, { addSuffix: true, locale: ko }),
    [date]
  );
  const formattedDate = useMemo(
    () => format(date, 'yyyy-MM-dd HH:mm:ss'),
    [date]
  );

  const categoryColors = {
    news: 'text-news hover:text-news-hover',
    community: 'text-community hover:text-community-hover',
    deals: 'text-deals hover:text-deals-hover',
  };
  
  return (
    <div 
      className="group relative flex flex-col overflow-hidden rounded-xl bg-white shadow-card transition-all hover:shadow-card-hover dark:bg-gray-800 dark:border-gray-700 cursor-pointer animate-fade-in"
      onClick={onClick}
    >
      <div className="aspect-video relative overflow-hidden rounded-t-xl">
        <Image
          src={thumbnail}
          alt={title}
          fill
          className="object-cover transition-transform duration-300 group-hover:scale-105"
          sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
        />
        {isNew && (
          <span className="absolute top-3 right-3 bg-red-500 text-white text-xs px-2 py-1 rounded-full font-medium animate-pulse">
            NEW
          </span>
        )}
      </div>

      <div className="flex flex-col flex-1 p-card">
        <div className="flex items-start justify-between gap-2 mb-2">
          <h3 className="font-medium line-clamp-2 group-hover:text-gray-600 dark:group-hover:text-gray-300">
            {title}
          </h3>
        </div>

        <div className="mt-auto pt-4 flex items-center justify-between text-sm text-gray-500">
          <div className="flex items-center space-x-2">
            <span className={categoryColors[category]}>{source}</span>
            <span title={formattedDate}>{timeAgo}</span>
          </div>

          <div className="flex items-center space-x-3">
            <button
              onClick={(e) => {
                e.stopPropagation();
                onLike?.();
              }}
              className="flex items-center space-x-1 hover:text-red-500 transition-colors"
            >
              <Heart
                size={16}
                className={isLiked ? 'fill-red-500 text-red-500' : ''}
              />
              <span>{likes}</span>
            </button>

            <button
              onClick={(e) => {
                e.stopPropagation();
                onBookmark?.();
              }}
              className="flex items-center space-x-1 hover:text-blue-500 transition-colors"
            >
              <Bookmark
                size={16}
                className={isBookmarked ? 'fill-blue-500 text-blue-500' : ''}
              />
              <span>{bookmarks}</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
