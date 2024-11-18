import { CATEGORIES } from '@/lib/constants';
import { ContentGrid } from '@/components/content/ContentGrid';

export default function DealsPage() {
  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold text-[#FF0000] mb-8">{CATEGORIES.deals}</h1>
      <ContentGrid category="deals" />
    </div>
  );
}
