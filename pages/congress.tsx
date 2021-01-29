import CongressGrid from '@components/CongressGrid/CongressGrid';
import Layout from '@components/Layout/Layout';
import React from 'react';
import {withApollo} from '@libs/with-apollo';
import CircularProgress from '@material-ui/core/CircularProgress';
import {makeStyles} from '@material-ui/core/styles';
import gql from 'graphql-tag';
import {useQuery} from '@apollo/react-hooks';

const GET_ELECTED_OFFICIALS = gql`
  query getElectedOfficials {
    elected_officials {
      id
      political_party_id
      member_id
      is_active
      position
      state
    }
  }
`;

const Congress = () => {
	const {loading, error, data} = useQuery(GET_ELECTED_OFFICIALS);
	const classes = useStyles();

	if (loading) {
		return (
			<div className={classes.root}>
				<CircularProgress/>
			</div>
		);
	}

	if (error) {
		return <span>Error {JSON.stringify(error, null, 2)}</span>;
	}

	if (data.elected_officials) {
		return (
			<Layout>
				<CongressGrid electedOfficials={data.elected_officials}/>
			</Layout>
		);
	}
};

const useStyles = makeStyles(() => ({
	root: {
		flexGrow: 1
	}
}));

export default withApollo({ssr: true})(Congress);
