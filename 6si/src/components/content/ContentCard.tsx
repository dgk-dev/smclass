"use client";

import { ContentCard as ContentCardType } from '@/types';
import Image from 'next/image';
import { format, formatDistanceToNow } from 'date-fns';
import { ko } from 'date-fns/locale';
import { useMemo } from 'react';

export function ContentCard({
  thumbnail,
  title,
  source,
  timestamp,
  isNew,
  category
}: ContentCardType) {
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
    <div className="group relative overflow-hidden rounded-lg border bg-white shadow-sm transition-all hover:shadow-md dark:bg-gray-800 dark:border-gray-700">
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
      </div>
    </div>
  );
}
