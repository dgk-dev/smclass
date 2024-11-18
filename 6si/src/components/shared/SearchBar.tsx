"use client";

import { useState } from 'react';
import { useRouter } from 'next/navigation';
import { Search } from 'lucide-react';

export function SearchBar() {
  const [query, setQuery] = useState('');
  const router = useRouter();

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault();
    if (query.trim()) {
      router.push(`/search?q=${encodeURIComponent(query)}`);
    }
  };

  return (
    <form onSubmit={handleSearch} className="relative w-full max-w-md">
      <input
        type="search"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="검색어를 입력하세요"
        className="w-full h-10 pl-4 pr-10 rounded-full bg-gray-50 border border-gray-200 text-gray-900 text-sm
          placeholder:text-gray-500
          focus:outline-none focus:border-brand-500 focus:ring-1 focus:ring-brand-500
          transition-colors"
      />
      <button
        type="submit"
        className="absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 hover:text-brand-500 transition-colors"
        aria-label="검색"
      >
        <Search className="w-5 h-5" />
      </button>
    </form>
  );
}
