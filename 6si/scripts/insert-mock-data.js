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

// Helper function to generate random numbers
const random = (min, max) => Math.floor(Math.random() * (max - min + 1)) + min;

// Helper function to generate past timestamp
const getPastTime = (hoursAgo) => new Date(now.getTime() - hoursAgo * 60 * 60 * 1000).toISOString();

// News sources
const newsSources = ['연합뉴스', '조선일보', '중앙일보', '동아일보', 'KBS', 'MBC', 'SBS', '한겨레', '매일경제', '한국경제', 'IT조선', '테크M', '블로터'];

// Community sources
const communitySources = ['디시인사이드', '루리웹', '클리앙', '뽐뿌', '82쿡', '인벤', '개드립', '오늘의유머', '더쿠', '네이트판', 'FM코리아', '보배드림'];

// Shopping sites
const dealSources = ['쿠팡', '11번가', 'G마켓', '옥션', '위메프', '티몬', '인터파크', 'SSG닷컴', '롯데온', '네이버쇼핑', '카카오쇼핑'];

// News topics and templates
const newsTopics = [
  { prefix: '삼성전자', templates: ['%s 신제품 출시 예정', '%s 실적 발표', '%s 신기술 개발', '%s 투자 계획 발표'] },
  { prefix: 'LG전자', templates: ['%s 신제품 공개', '%s 신규 사업 진출', '%s 특허 획득', '%s 글로벌 시장 확대'] },
  { prefix: '현대차', templates: ['%s 전기차 라인업 확대', '%s 자율주행 기술 개발', '%s 신모델 출시', '%s 해외 공장 설립'] },
  { prefix: '카카오', templates: ['%s 신규 서비스 출시', '%s AI 기술 도입', '%s 플랫폼 확장', '%s 제휴 확대'] },
  { prefix: '네이버', templates: ['%s 클라우드 사업 강화', '%s 커머스 플랫폼 개편', '%s 해외 진출', '%s 신규 투자'] },
];

// Generate mock news
const generateMockNews = (count) => {
  const news = [];
  for (let i = 0; i < count; i++) {
    const topic = newsTopics[random(0, newsTopics.length - 1)];
    const template = topic.templates[random(0, topic.templates.length - 1)];
    const title = template.replace('%s', topic.prefix);
    const source = newsSources[random(0, newsSources.length - 1)];
    
    news.push({
      id: uuidv4(),
      title,
      thumbnail: `https://picsum.photos/seed/news${i}/800/600`,
      source,
      category: 'news',
      url: `https://example.com/news/${i}`,
      timestamp: getPastTime(random(0, 72)),
      likes: random(0, 1000),
      bookmarks: random(0, 500),
      created_at: now.toISOString(),
    });
  }
  return news;
};

// Community post templates
const communityTemplates = [
  '오늘 %s 다녀왔어요 (후기)',
  '%s 추천해주세요!',
  '%s 어떻게 생각하시나요?',
  '%s 정보 공유합니다',
  '요즘 %s 괜찮나요?',
  '%s 리뷰입니다',
  '%s 꿀팁 공유',
  '[스압] %s 완벽 정리',
  '%s 질문이요~',
  '드디어 %s 했습니다!!',
];

const communityTopics = [
  '맛집', '카페', '여행', '운동', '게임', '직장', '학교', '취미',
  '음식', '영화', '드라마', '음악', '책', '공부', '취업', '연애',
  '결혼', '육아', '반려동물', '주식', '부동산', '자동차', '컴퓨터', '스마트폰'
];

// Generate mock community posts
const generateMockCommunity = (count) => {
  const posts = [];
  for (let i = 0; i < count; i++) {
    const template = communityTemplates[random(0, communityTemplates.length - 1)];
    const topic = communityTopics[random(0, communityTopics.length - 1)];
    const title = template.replace('%s', topic);
    const source = communitySources[random(0, communitySources.length - 1)];
    
    posts.push({
      id: uuidv4(),
      title,
      thumbnail: `https://picsum.photos/seed/community${i}/800/600`,
      source,
      category: 'community',
      url: `https://example.com/community/${i}`,
      timestamp: getPastTime(random(0, 48)),
      likes: random(0, 2000),
      bookmarks: random(0, 1000),
      created_at: now.toISOString(),
    });
  }
  return posts;
};

// Deal templates
const dealTemplates = [
  '[%s] %s 특가 행사',
  '[단독] %s %s 최저가',
  '[오늘만] %s %s 할인',
  '[초특가] %s %s 세일',
  '[빅세일] %s %s 특별가',
  '[쎈딜] %s %s 파격특가',
  '[최저가] %s %s 기획전',
  '[타임딜] %s %s 특가',
];

const dealProducts = [
  '삼성 TV', 'LG 냉장고', '애플 아이폰', '다이슨 청소기', '쿠쿠 밥솥',
  '에어팟 프로', '갤럭시 버즈', '소니 헤드폰', '닌텐도 스위치', 'PS5',
  '맥북 프로', '갤럭시북', '아이패드', '갤럭시탭', '샤오미 로봇청소기',
  '모니터', '키보드', '마우스', '게이밍 의자', '공기청정기',
  '건조기', '세탁기', '식기세척기', '전자레인지', '에어컨'
];

// Generate mock deals
const generateMockDeals = (count) => {
  const deals = [];
  for (let i = 0; i < count; i++) {
    const template = dealTemplates[random(0, dealTemplates.length - 1)];
    const product = dealProducts[random(0, dealProducts.length - 1)];
    const source = dealSources[random(0, dealSources.length - 1)];
    const title = template.replace('%s', source).replace('%s', product);
    
    deals.push({
      id: uuidv4(),
      title,
      thumbnail: `https://picsum.photos/seed/deals${i}/800/600`,
      source,
      category: 'deals',
      url: `https://example.com/deals/${i}`,
      timestamp: getPastTime(random(0, 24)),
      likes: random(0, 3000),
      bookmarks: random(0, 1500),
      created_at: now.toISOString(),
    });
  }
  return deals;
};

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

    // Generate 100 items for each category
    const mockNews = generateMockNews(100);
    const mockCommunity = generateMockCommunity(100);
    const mockDeals = generateMockDeals(100);

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
