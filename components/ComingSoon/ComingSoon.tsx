import React from 'react';
import Image from 'next/image';
import {makeStyles} from '@material-ui/core/styles';

const ComingSoon = () => {
	const classes = useStyles();
	return (
		<div className={classes.root}>
			<div className={classes.container}>
				<Image
					src="/barrier.svg"
					alt="construction barrier"
					width={150}
					height={150}
				/>
				<h1>Coming Soon</h1>
			</div>
		</div>
	);
};

const useStyles = makeStyles(() => ({
	root: {
		height: '90vh',
		display: 'flex',
		justifyContent: 'center',
		alignItems: 'center'
	},
	container: {
		alignItems: 'center',
		textAlign: 'center'
	}
}));

export default ComingSoon;
