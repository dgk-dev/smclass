import { CATEGORIES } from '@/lib/constants';
import Link from 'next/link';

export default function Home() {
  return (
    <div className="container mx-auto px-4 py-8">
      {/* News Section */}
      <section className="mb-12">
        <div className="flex justify-between items-center mb-6">
          <h2 className="text-2xl font-bold text-[#0066FF]">{CATEGORIES.news}</h2>
          <Link 
            href="/section/news"
            className="text-sm text-gray-600 hover:text-[#0066FF]"
          >
            더보기 →
          </Link>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {/* Content cards will be added here */}
        </div>
      </section>

      {/* Community Section */}
      <section className="mb-12">
        <div className="flex justify-between items-center mb-6">
          <h2 className="text-2xl font-bold text-[#00CC00]">{CATEGORIES.community}</h2>
          <Link 
            href="/section/community"
            className="text-sm text-gray-600 hover:text-[#00CC00]"
          >
            더보기 →
          </Link>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {/* Content cards will be added here */}
        </div>
      </section>

      {/* Deals Section */}
      <section className="mb-12">
        <div className="flex justify-between items-center mb-6">
          <h2 className="text-2xl font-bold text-[#FF0000]">{CATEGORIES.deals}</h2>
          <Link 
            href="/section/deals"
            className="text-sm text-gray-600 hover:text-[#FF0000]"
          >
            더보기 →
          </Link>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {/* Content cards will be added here */}
        </div>
      </section>
    </div>
  );
}
