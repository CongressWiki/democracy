import Head from 'next/head'
import Link from 'next/link'
import ProposalsTableSubscription from '../components/ProposalsTable'
import styles from '../styles/Proposals.module.css'
import { withApollo } from '../lib/withApollo'

function Votes() {
  return (
    <div className={styles.container}>
      <Head>
        <title>Keeping US Accountable</title>
        <link rel='icon' href='/favicon.ico' />
      </Head>

      <main className={styles.main}>
        <h1 className={styles.title}>USA Counts</h1>

        <p className={styles.description}>
          Do our elected officials vote for us?
        </p>
        <Link href='/'>
            <a>
              <h3>&larr; Home</h3>
            </a>
          </Link>

        <div className={styles.grid}>
          <ProposalsTableSubscription />
        </div>
      </main>
    </div>
  )
}

export default withApollo({ ssr: true })(Votes)
