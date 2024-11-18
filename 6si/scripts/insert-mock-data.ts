import { createClient } from '@supabase/supabase-js';
import dotenv from 'dotenv';

dotenv.config({ path: '.env.local' });

const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL!;
const supabaseKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!;

const supabase = createClient(supabaseUrl, supabaseKey);

const mockNews = [
  {
    title: '삼성전자, 새로운 AI 칩 개발 발표',
    thumbnail: 'https://picsum.photos/seed/news1/800/600',
    source: '테크뉴스',
    category: 'news',
    url: 'https://example.com/news1',
    timestamp: new Date().toISOString(),
  },
  {
    title: 'LG전자, 혁신적인 스마트홈 시스템 출시',
    thumbnail: 'https://picsum.photos/seed/news2/800/600',
    source: '전자신문',
    category: 'news',
    url: 'https://example.com/news2',
    timestamp: new Date(Date.now() - 2 * 60 * 60 * 1000).toISOString(),
  },
  {
    title: '현대자동차, 자율주행 기술 혁신 성과 공개',
    thumbnail: 'https://picsum.photos/seed/news3/800/600',
    source: '자동차신문',
    category: 'news',
    url: 'https://example.com/news3',
    timestamp: new Date(Date.now() - 4 * 60 * 60 * 1000).toISOString(),
  }
];

const mockCommunity = [
  {
    title: '오늘 처음으로 리액트 배워봤어요!',
    thumbnail: 'https://picsum.photos/seed/community1/800/600',
    source: '개발자커뮤니티',
    category: 'community',
    url: 'https://example.com/community1',
    timestamp: new Date().toISOString(),
  },
  {
    title: '주말에 등산 같이 가실 분?',
    thumbnail: 'https://picsum.photos/seed/community2/800/600',
    source: '취미커뮤니티',
    category: 'community',
    url: 'https://example.com/community2',
    timestamp: new Date(Date.now() - 3 * 60 * 60 * 1000).toISOString(),
  },
  {
    title: '오늘 먹은 맛집 추천합니다!',
    thumbnail: 'https://picsum.photos/seed/community3/800/600',
    source: '맛집커뮤니티',
    category: 'community',
    url: 'https://example.com/community3',
    timestamp: new Date(Date.now() - 5 * 60 * 60 * 1000).toISOString(),
  }
];

const mockDeals = [
  {
    title: '[쿠팡] 애플 에어팟 프로 2세대 특가',
    thumbnail: 'https://picsum.photos/seed/deals1/800/600',
    source: '쿠팡',
    category: 'deals',
    url: 'https://example.com/deals1',
    timestamp: new Date().toISOString(),
  },
  {
    title: '[11번가] 삼성 TV 블랙프라이데이 특가',
    thumbnail: 'https://picsum.photos/seed/deals2/800/600',
    source: '11번가',
    category: 'deals',
    url: 'https://example.com/deals2',
    timestamp: new Date(Date.now() - 1 * 60 * 60 * 1000).toISOString(),
  },
  {
    title: '[G마켓] 노트북 초특가 세일',
    thumbnail: 'https://picsum.photos/seed/deals3/800/600',
    source: 'G마켓',
    category: 'deals',
    url: 'https://example.com/deals3',
    timestamp: new Date(Date.now() - 6 * 60 * 60 * 1000).toISOString(),
  }
];

async function insertMockData() {
  try {
    // Clear existing data
    await supabase.from('contents').delete().neq('id', '00000000-0000-0000-0000-000000000000');

    // Insert mock data
    const allMockData = [...mockNews, ...mockCommunity, ...mockDeals];
    const { data, error } = await supabase.from('contents').insert(allMockData);

    if (error) {
      console.error('Error inserting mock data:', error);
      return;
    }

    console.log('Successfully inserted mock data:', data);
  } catch (error) {
    console.error('Error:', error);
  }
}

insertMockData();
