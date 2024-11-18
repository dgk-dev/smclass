const { createClient } = require('@supabase/supabase-js');
const dotenv = require('dotenv');
const path = require('path');
const { v4: uuidv4 } = require('uuid');

dotenv.config({ path: path.resolve(__dirname, '../.env.local') });

const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL;
const supabaseKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY;

if (!supabaseUrl || !supabaseKey) {
  console.error('Missing Supabase credentials in .env.local');
  process.exit(1);
}

const supabase = createClient(supabaseUrl, supabaseKey);

const now = new Date();

const mockNews = [
  {
    id: uuidv4(),
    title: '삼성전자, 새로운 AI 칩 개발 발표',
    thumbnail: 'https://picsum.photos/seed/news1/800/600',
    source: '테크뉴스',
    category: 'news',
    url: 'https://example.com/news1',
    timestamp: now.toISOString(),
    likes: 0,
    bookmarks: 0,
    created_at: now.toISOString(),
  },
  {
    id: uuidv4(),
    title: 'LG전자, 혁신적인 스마트홈 시스템 출시',
    thumbnail: 'https://picsum.photos/seed/news2/800/600',
    source: '전자신문',
    category: 'news',
    url: 'https://example.com/news2',
    timestamp: new Date(now.getTime() - 2 * 60 * 60 * 1000).toISOString(),
    likes: 0,
    bookmarks: 0,
    created_at: now.toISOString(),
  },
  {
    id: uuidv4(),
    title: '현대자동차, 자율주행 기술 혁신 성과 공개',
    thumbnail: 'https://picsum.photos/seed/news3/800/600',
    source: '자동차신문',
    category: 'news',
    url: 'https://example.com/news3',
    timestamp: new Date(now.getTime() - 4 * 60 * 60 * 1000).toISOString(),
    likes: 0,
    bookmarks: 0,
    created_at: now.toISOString(),
  }
];

const mockCommunity = [
  {
    id: uuidv4(),
    title: '오늘 처음으로 리액트 배워봤어요!',
    thumbnail: 'https://picsum.photos/seed/community1/800/600',
    source: '개발자커뮤니티',
    category: 'community',
    url: 'https://example.com/community1',
    timestamp: now.toISOString(),
    likes: 0,
    bookmarks: 0,
    created_at: now.toISOString(),
  },
  {
    id: uuidv4(),
    title: '주말에 등산 같이 가실 분?',
    thumbnail: 'https://picsum.photos/seed/community2/800/600',
    source: '취미커뮤니티',
    category: 'community',
    url: 'https://example.com/community2',
    timestamp: new Date(now.getTime() - 3 * 60 * 60 * 1000).toISOString(),
    likes: 0,
    bookmarks: 0,
    created_at: now.toISOString(),
  },
  {
    id: uuidv4(),
    title: '오늘 먹은 맛집 추천합니다!',
    thumbnail: 'https://picsum.photos/seed/community3/800/600',
    source: '맛집커뮤니티',
    category: 'community',
    url: 'https://example.com/community3',
    timestamp: new Date(now.getTime() - 5 * 60 * 60 * 1000).toISOString(),
    likes: 0,
    bookmarks: 0,
    created_at: now.toISOString(),
  }
];

const mockDeals = [
  {
    id: uuidv4(),
    title: '[쿠팡] 애플 에어팟 프로 2세대 특가',
    thumbnail: 'https://picsum.photos/seed/deals1/800/600',
    source: '쿠팡',
    category: 'deals',
    url: 'https://example.com/deals1',
    timestamp: now.toISOString(),
    likes: 0,
    bookmarks: 0,
    created_at: now.toISOString(),
  },
  {
    id: uuidv4(),
    title: '[11번가] 삼성 TV 블랙프라이데이 특가',
    thumbnail: 'https://picsum.photos/seed/deals2/800/600',
    source: '11번가',
    category: 'deals',
    url: 'https://example.com/deals2',
    timestamp: new Date(now.getTime() - 1 * 60 * 60 * 1000).toISOString(),
    likes: 0,
    bookmarks: 0,
    created_at: now.toISOString(),
  },
  {
    id: uuidv4(),
    title: '[G마켓] 노트북 초특가 세일',
    thumbnail: 'https://picsum.photos/seed/deals3/800/600',
    source: 'G마켓',
    category: 'deals',
    url: 'https://example.com/deals3',
    timestamp: new Date(now.getTime() - 6 * 60 * 60 * 1000).toISOString(),
    likes: 0,
    bookmarks: 0,
    created_at: now.toISOString(),
  }
];

async function insertMockData() {
  try {
    // Clear existing data
    const { error: deleteError } = await supabase
      .from('contents')
      .delete()
      .neq('id', '00000000-0000-0000-0000-000000000000');

    if (deleteError) {
      console.error('Error deleting existing data:', deleteError);
      return;
    }

    // Insert mock data
    const allMockData = [...mockNews, ...mockCommunity, ...mockDeals];
    const { data, error: insertError } = await supabase
      .from('contents')
      .insert(allMockData)
      .select();

    if (insertError) {
      console.error('Error inserting mock data:', insertError);
      return;
    }

    console.log('Successfully inserted mock data:', data?.length, 'items');
  } catch (error) {
    console.error('Error:', error);
  } finally {
    process.exit(0);
  }
}

insertMockData();
