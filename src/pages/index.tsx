import Layout, {siteTitle} from '../components/Layout';

import Bubble from '../components/atoms/Bubble'
import BubblesLine from '../components/molecules/BubblesLine'
import Head from 'next/head';

export default function Home() {
	return (
		<Layout home>
			<Head>
				<title>{siteTitle}</title>
      </Head>
      <BubblesLine>
        <Bubble src="/images/profile.jpg" />
        <Bubble src="/images/profile.jpg" />
        <Bubble src="/images/profile.jpg" />
        <Bubble src="/images/profile.jpg" />
      </BubblesLine>
		</Layout>
	);
}
