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
      bgHover: 'hover:bg-accent-blue/5',
    },
    community: {
      color: 'text-accent-green',
      bgHover: 'hover:bg-accent-green/5',
    },
    deals: {
      color: 'text-accent-red',
      bgHover: 'hover:bg-accent-red/5',
    },
  };
  
  return (
    <div 
      className="group flex flex-col overflow-hidden bg-surface-50 border border-surface-200 rounded-2xl shadow-surface transition-all hover:shadow-surface-hover hover:border-surface-300 cursor-pointer animate-fade-in"
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
            <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-accent-red text-white">
              NEW
            </span>
          </div>
        )}
      </div>

      <div className="flex flex-col flex-1 p-5">
        <div className="flex items-start justify-between gap-4 mb-3">
          <h3 className="text-lg font-medium text-surface-900 line-clamp-2 group-hover:text-brand-800 transition-colors">
            {title}
          </h3>
        </div>

        <div className="mt-auto pt-4 flex items-center justify-between border-t border-surface-200">
          <div className="flex items-center gap-3">
            <span 
              className={`text-sm font-medium ${categoryConfig[category].color}`}
            >
              {source}
            </span>
            <time 
              dateTime={formattedDate}
              className="text-sm text-surface-500"
              title={formattedDate}
            >
              {timeAgo}
            </time>
          </div>

          <div className="flex items-center gap-4">
            <button
              onClick={(e) => {
                e.stopPropagation();
                onLike?.();
              }}
              className={`group/btn flex items-center gap-1.5 ${
                categoryConfig[category].bgHover
              } rounded-full px-2.5 py-1.5 transition-colors`}
            >
              <Heart
                size={14}
                className={`transition-colors ${
                  isLiked ? 'fill-accent-red text-accent-red' : 'text-surface-500 group-hover/btn:text-accent-red'
                }`}
              />
              <span className={`text-xs ${
                isLiked ? 'text-accent-red' : 'text-surface-500 group-hover/btn:text-accent-red'
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
              } rounded-full px-2.5 py-1.5 transition-colors`}
            >
              <Bookmark
                size={14}
                className={`transition-colors ${
                  isBookmarked ? 'fill-accent-blue text-accent-blue' : 'text-surface-500 group-hover/btn:text-accent-blue'
                }`}
              />
              <span className={`text-xs ${
                isBookmarked ? 'text-accent-blue' : 'text-surface-500 group-hover/btn:text-accent-blue'
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
