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

  const categoryConfig = {
    news: {
      color: 'text-accent-blue',
      bgHover: 'hover:bg-brand-50',
    },
    community: {
      color: 'text-accent-green',
      bgHover: 'hover:bg-brand-50',
    },
    deals: {
      color: 'text-accent-red',
      bgHover: 'hover:bg-brand-50',
    },
  };
  
  return (
    <div 
      className="group flex overflow-hidden bg-white hover:bg-gray-50 cursor-pointer animate-fade-in transition-all"
      onClick={onClick}
    >
      {/* Thumbnail */}
      <div className="relative w-24 h-16 sm:w-32 sm:h-20 shrink-0">
        <Image
          src={thumbnail}
          alt={title}
          fill
          className="object-cover rounded-sm transition-transform duration-300 group-hover:scale-[1.02]"
          sizes="(max-width: 768px) 96px, 128px"
        />
        {isNew && (
          <div className="absolute top-1 right-1">
            <span className="inline-flex items-center px-1.5 py-0.5 rounded-full text-[10px] font-medium bg-accent-red text-white">
              N
            </span>
          </div>
        )}
      </div>

      {/* Content */}
      <div className="flex flex-col flex-1 min-w-0 p-2 sm:p-3">
        <div className="flex items-start justify-between gap-2 mb-1">
          <h3 className="text-sm sm:text-base font-medium text-gray-900 line-clamp-1 group-hover:text-brand-600 transition-colors">
            {title}
          </h3>
        </div>

        <div className="mt-auto flex items-center justify-between">
          <div className="flex items-center gap-2 min-w-0">
            <span className={`text-xs font-medium truncate ${categoryConfig[category].color}`}>
              {source}
            </span>
            <time 
              dateTime={formattedDate}
              className="text-xs text-gray-500 truncate"
              title={formattedDate}
            >
              {timeAgo}
            </time>
          </div>

          <div className="flex items-center gap-2 shrink-0">
            <button
              onClick={(e) => {
                e.stopPropagation();
                onLike?.();
              }}
              className={`group/btn flex items-center gap-1 ${categoryConfig[category].bgHover} rounded-full px-1.5 py-0.5 transition-colors`}
            >
              <Heart
                size={12}
                className={`transition-colors ${
                  isLiked ? 'fill-accent-red text-accent-red' : 'text-gray-400 group-hover/btn:text-accent-red'
                }`}
              />
              <span className={`text-[10px] ${
                isLiked ? 'text-accent-red' : 'text-gray-500 group-hover/btn:text-accent-red'
              }`}>
                {likes}
              </span>
            </button>

            <button
              onClick={(e) => {
                e.stopPropagation();
                onBookmark?.();
              }}
              className={`group/btn flex items-center gap-1 ${categoryConfig[category].bgHover} rounded-full px-1.5 py-0.5 transition-colors`}
            >
              <Bookmark
                size={12}
                className={`transition-colors ${
                  isBookmarked ? 'fill-accent-blue text-accent-blue' : 'text-gray-400 group-hover/btn:text-accent-blue'
                }`}
              />
              <span className={`text-[10px] ${
                isBookmarked ? 'text-accent-blue' : 'text-gray-500 group-hover/btn:text-accent-blue'
              }`}>
                {bookmarks}
              </span>
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
