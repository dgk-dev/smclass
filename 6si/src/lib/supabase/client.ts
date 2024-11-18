import { createClientComponentClient } from '@supabase/auth-helpers-nextjs';
import { Database } from './database.types';

export const createClient = () => {
  try {
    return createClientComponentClient<Database>();
  } catch (error) {
    console.error('Failed to create Supabase client:', error);
    throw new Error('Failed to initialize Supabase client. Please check your environment variables.');
  }
};
