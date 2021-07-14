import * as React from 'react';
import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import TextField from '@material-ui/core/TextField';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import Checkbox from '@material-ui/core/Checkbox';
import Link from '@material-ui/core/Link';
import Grid from '@material-ui/core/Grid';
import Box from '@material-ui/core/Box';
import LockOutlinedIcon from '@material-ui/icons/LockOutlined';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';
import axios from 'axios';
//import { useState } from 'react';

/*
  *****コメントを読んで下さい*****
  よくわからなかったため，今回　material ui のバージョンを上げました．
  *****必ず npm install を実行してください．*****
  したがって，他の箇所のコードが動かないことが発生しており，一時的にすべてコメントアウト
  しています．
  これらを解決する際には公式サイトのリファレンスを参考にしてください．
  https://next.material-ui.com/
  このサイトはMaterial Uiのバージョン5について書かれています．
  このログインページを開くには /login をつけてアクセスしてください．
  またこのテンプレートはMaterial UIのGithubから持ってきました．
  https://github.com/mui-org/material-ui/blob/next/docs/src/pages/getting-started/templates/sign-in/SignIn.tsx
*/
function Copyright(props: any) {
  return (
    <Typography variant="body2" color="text.secondary" align="center" {...props}>
      {'Copyright © '}
      <Link color="inherit" href="https://material-ui.com/">
        Team1
      </Link>{' '}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
}

export default function SignIn() {
  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    // eslint-disable-next-line no-console
    // ここのconsole.logによってF12を押すと表示されるコンソールに
    // ID: ---, password:----,が表示されていると思います．
    // ここに idとパスワードを送信するPOSTに機能を記述またはインポートしてサーバーと通信できるように
    // 設定お願いします．
    // eslint-disable-next-line
    var params = new URLSearchParams();
    // dataはnullが含まれているためnullチェックを行うかつ文字列型にキャスト
    const username = data.get('id')?.toString()
    const password = data.get('password')?.toString()

    if (username != null && password != null) {
      params.append('username', username)
      params.append('password', password)
    }
    // 変数定義
    let res
    try {
      res = await axios.post('http://localhost:8000/token', params)
    } catch(err){
      res = err.response
    }
    // なにかしらエラーが発生した場合の処理(デバッグ)
    if (res.status !== 200) {
      console.log({
        message: res.data.detail
      })
    }
    else {
      // ログインが成功したらマイページに飛ぶ
      localStorage.setItem('token',res.data.access_token) //localstrageにアクセストークンを保存
    window.location.href = 'http://localhost:8000/getSub/'; // 通常の遷移 
    }
    
    // debug
    console.log(res)
    console.log({
      status: res.status,
    })
    console.log({
      ID: username,
      password: password,
    });
  };

  return (
    <Container component="main" maxWidth="xs">
      <CssBaseline />
      <Box
        sx={{
          marginTop: 8,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
        }}
      >
        <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
          <LockOutlinedIcon />
        </Avatar>
        <Typography component="h1" variant="h5">
          Team 1
        </Typography>
        <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
          <TextField
            margin="normal"
            required
            fullWidth
            id="id"
            label="ID"
            name="id"
            autoComplete="id"
            autoFocus
          />
          <TextField
            margin="normal"
            required
            fullWidth
            name="password"
            label="Password"
            type="password"
            id="password"
            autoComplete="current-password"
          />
          <FormControlLabel
            control={<Checkbox value="remember" color="primary" />}
            label="Remember me"
          />
          <Button type="submit" fullWidth variant="contained" sx={{ mt: 3, mb: 2 }}>
            ログイン
          </Button>
          <Grid container>
            <Grid item xs>
              <Link href="#" variant="body2">
                Forgot password?
              </Link>
            </Grid>
            <Grid item>
              <Link href="#" variant="body2">
                {"Don't have an account? Sign Up"}
              </Link>
            </Grid>
          </Grid>
        </Box>
      </Box>
      <Copyright sx={{ mt: 8, mb: 4 }} />
    </Container>
  );
}