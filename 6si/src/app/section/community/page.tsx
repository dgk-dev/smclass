import { CATEGORIES } from '@/lib/constants';
import { ContentGrid } from '@/components/content/ContentGrid';

export default function CommunityPage() {
  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold text-[#00CC00] mb-8">{CATEGORIES.community}</h1>
      <ContentGrid category="community" />
    </div>
  );
}
