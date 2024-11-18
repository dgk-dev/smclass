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
      className="group flex flex-col overflow-hidden bg-white rounded-lg border border-gray-200 shadow-card transition-all hover:shadow-card-hover hover:border-gray-300 cursor-pointer animate-fade-in"
      onClick={onClick}
    >
      <div className="relative aspect-[1.91/1] overflow-hidden">
        <Image
          src={thumbnail}
          alt={title}
          fill
          className="object-cover transition-transform duration-300 group-hover:scale-[1.02]"
          sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
        />
        {isNew && (
          <div className="absolute top-3 right-3">
            <span className="inline-flex items-center px-2.5 py-1 rounded-full text-xs font-medium bg-accent-red text-white">
              NEW
            </span>
          </div>
        )}
      </div>

      <div className="flex flex-col flex-1 p-4">
        <div className="flex items-start justify-between gap-4 mb-3">
          <h3 className="text-base font-medium text-gray-900 line-clamp-2 group-hover:text-brand-600 transition-colors">
            {title}
          </h3>
        </div>

        <div className="mt-auto pt-4 flex items-center justify-between border-t border-gray-100">
          <div className="flex items-center gap-3">
            <span 
              className={`text-sm font-medium ${categoryConfig[category].color}`}
            >
              {source}
            </span>
            <time 
              dateTime={formattedDate}
              className="text-sm text-gray-500"
              title={formattedDate}
            >
              {timeAgo}
            </time>
          </div>

          <div className="flex items-center gap-3">
            <button
              onClick={(e) => {
                e.stopPropagation();
                onLike?.();
              }}
              className={`group/btn flex items-center gap-1.5 ${
                categoryConfig[category].bgHover
              } rounded-full px-2 py-1 transition-colors`}
            >
              <Heart
                size={14}
                className={`transition-colors ${
                  isLiked ? 'fill-accent-red text-accent-red' : 'text-gray-400 group-hover/btn:text-accent-red'
                }`}
              />
              <span className={`text-xs ${
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
              className={`group/btn flex items-center gap-1.5 ${
                categoryConfig[category].bgHover
              } rounded-full px-2 py-1 transition-colors`}
            >
              <Bookmark
                size={14}
                className={`transition-colors ${
                  isBookmarked ? 'fill-accent-blue text-accent-blue' : 'text-gray-400 group-hover/btn:text-accent-blue'
                }`}
              />
              <span className={`text-xs ${
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
