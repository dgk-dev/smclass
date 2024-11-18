import { ContentCard as ContentCardType } from '@/types';
import Image from 'next/image';
import { formatDistanceToNow } from 'date-fns';
import { ko } from 'date-fns/locale';

export function ContentCard({
  thumbnail,
  title,
  source,
  timestamp,
  isNew,
  category
}: ContentCardType) {
  return (
    <div className="group relative overflow-hidden rounded-lg border border-gray-100 bg-white transition-all hover:shadow-lg hover:border-gray-200">
      <div className="aspect-video relative overflow-hidden">
        <Image
          src={thumbnail}
          alt={title}
          fill
          className="object-cover transition-transform group-hover:scale-105"
        />
        {isNew && (
          <span className="absolute top-2 right-2 bg-brand-500 text-white text-xs px-2 py-1 rounded-full">
            NEW
          </span>
        )}
      </div>
      <div className="p-4">
        <h3 className="text-lg font-medium text-gray-900 line-clamp-2 mb-2 group-hover:text-brand-600 transition-colors">
          {title}
        </h3>
        <div className="flex items-center justify-between text-sm text-gray-500">
          <span className="font-medium">{source}</span>
          <time dateTime={timestamp.toISOString()} className="text-gray-400">
            {formatDistanceToNow(timestamp, { addSuffix: true, locale: ko })}
          </time>
        </div>
      </div>
    </div>
  );
}
