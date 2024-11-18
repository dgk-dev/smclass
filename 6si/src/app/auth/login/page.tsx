import { Auth } from '@supabase/auth-ui-react';
import { ThemeSupa } from '@supabase/auth-ui-shared';
import { createClient } from '@/lib/supabase/client';

export default function LoginPage() {
  const supabase = createClient();

  return (
    <div className="container mx-auto max-w-md p-8">
      <h1 className="text-2xl font-bold mb-8 text-center">로그인</h1>
      <Auth
        supabaseClient={supabase}
        appearance={{ theme: ThemeSupa }}
        providers={['google', 'github']}
        localization={{
          variables: {
            sign_in: {
              email_label: '이메일',
              password_label: '비밀번호',
              email_input_placeholder: '이메일 주소를 입력하세요',
              password_input_placeholder: '비밀번호를 입력하세요',
              button_label: '로그인',
              loading_button_label: '로그인 중...',
            },
            sign_up: {
              email_label: '이메일',
              password_label: '비밀번호',
              email_input_placeholder: '이메일 주소를 입력하세요',
              password_input_placeholder: '비밀번호를 입력하세요',
              button_label: '회원가입',
              loading_button_label: '회원가입 중...',
            },
          },
        }}
        theme="dark"
      />
    </div>
  );
}
