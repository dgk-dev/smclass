import { CATEGORIES } from '@/lib/constants';
import { ContentGrid } from '@/components/content/ContentGrid';

export default function NewsPage() {
  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold text-[#0066FF] mb-8">{CATEGORIES.news}</h1>
      <ContentGrid category="news" />
    </div>
  );
}
