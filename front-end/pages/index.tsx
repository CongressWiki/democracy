import BillsTable from '../components/BillsTable'
import Head from 'next/head'
import Link from 'next/link'
import styles from '../styles/Home.module.css'
import { withApollo } from '../lib/withApollo'

function Home() {
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

        <div className={styles.grid}>
          <BillsTable />
        </div>

        {/* <div className={styles.grid}>
          <Link href='/proposals'>
            <a className={styles.card}>
              <h3>House of Congress &rarr;</h3>
              <p>Track the latest votes held by the House of Representatives.</p>
            </a>
          </Link>

          <Link href='/proposals'>
            <a href='https://nextjs.org/docs' className={styles.card}>
              <h3>Senate &rarr;</h3>
              <p>Track the latest votes held by Senators.</p>
            </a>
          </Link>

          <Link href='/proposals'>
            <a
              href='https://github.com/vercel/next.js/tree/master/examples'
              className={styles.card}
            >
              <h3>Supreme Court &rarr;</h3>
              <p>Track the latest votes held by Supreme court justices.</p>
            </a>
          </Link>

          <Link href='/proposals'>
            <a
              href='https://github.com/vercel/next.js/tree/master/examples'
              className={styles.card}
            >
              <h3>Executive Office &rarr;</h3>
              <p>Track the latest orders signed by the President's cabinet.</p>
            </a>
          </Link>
        </div> */}
      </main>

      {/* <footer className={styles.footer}>
        <a
          href='https://vercel.com?utm_source=create-next-app&utm_medium=default-template&utm_campaign=create-next-app'
          target='_blank'
          rel='noopener noreferrer'
        >
          Powered by{' '}
          <img src='/vercel.svg' alt='Parker Logo' className={styles.logo} />
        </a>
      </footer> */}
    </div>
  )
}

export default withApollo()(Home)
