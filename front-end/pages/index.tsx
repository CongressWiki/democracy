import BillCanvas from '../components/BillCanvas'
import Head from 'next/head'
import { withApollo } from '../lib/withApollo'

function Home() {
  return (
    <div>
      <Head>
        <title>Keeping US Accountable</title>
        <link rel='icon' href='/favicon.ico' />
      </Head>
      <main>
        <h1>USA Counts</h1>
        <p>Do our elected officials vote for us?</p>
        <div>
          <BillCanvas />
        </div>
      </main>
    </div>
  )
}

export default withApollo()(Home)
