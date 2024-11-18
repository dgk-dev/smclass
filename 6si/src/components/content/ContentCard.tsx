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
  
  return (
    <div 
      className="group relative overflow-hidden rounded-lg border bg-white shadow-sm transition-all hover:shadow-md dark:bg-gray-800 dark:border-gray-700 cursor-pointer" 
      onClick={onClick}
    >
      <div className="aspect-video relative overflow-hidden">
        <Image
          src={thumbnail}
          alt={title}
          fill
          className="object-cover transition-transform group-hover:scale-105"
        />
        {isNew && (
          <span className="absolute top-2 right-2 bg-red-500 text-white text-xs px-2 py-1 rounded">
            NEW
          </span>
        )}
      </div>
      <div className="p-4">
        <h3 className="text-lg font-semibold line-clamp-2 mb-2">{title}</h3>
        <div className="flex items-center justify-between text-sm text-gray-500">
          <span>{source}</span>
          <time dateTime={formattedDate} title={formattedDate}>
            {timeAgo}
          </time>
        </div>
        <div className="flex items-center justify-between mt-2 text-sm text-gray-500">
          <button 
            onClick={(e) => {
              e.stopPropagation();
              onLike?.();
            }}
            className={`flex items-center gap-1 ${isLiked ? 'text-red-500' : ''}`}
          >
            <Heart size={16} className={isLiked ? 'fill-current' : ''} />
            <span>{likes}</span>
          </button>
          <button
            onClick={(e) => {
              e.stopPropagation();
              onBookmark?.();
            }}
            className={`flex items-center gap-1 ${isBookmarked ? 'text-blue-500' : ''}`}
          >
            <Bookmark size={16} className={isBookmarked ? 'fill-current' : ''} />
            <span>{bookmarks}</span>
          </button>
        </div>
      </div>
    </div>
  );
}
