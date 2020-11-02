import Layout, {siteTitle} from '../components/Layout';

import BubblesLine from '../components/molecules/BubblesLine'
import Head from 'next/head';

export default function Home() {
	return (
		<Layout home>
			<Head>
				<title>{siteTitle}</title>
      </Head>
      <BubblesLine />
		</Layout>
	);
}
