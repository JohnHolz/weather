import type { AppProps } from 'next/app'
import DefaultLayout from '../src/layouts/DefaultLayout'
import '../styles/globals.css'

const App = ({ Component, pageProps }: AppProps) => (
  <DefaultLayout>
    <Component {...pageProps} />
  </DefaultLayout>)

export default App