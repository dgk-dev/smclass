export const COLORS = {
  news: '#0066FF',
  community: '#00CC00',
  deals: '#FF0000',
} as const;

export const CATEGORIES = {
  news: '뉴스',
  community: '커뮤니티',
  deals: '할인정보',
} as const;

export type Category = keyof typeof CATEGORIES;

export const CONTENT_UPDATE_INTERVAL = 1000 * 60 * 60 * 6; // 6 hours
