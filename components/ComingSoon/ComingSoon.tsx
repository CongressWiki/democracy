import React from 'react';
import {makeStyles} from '@material-ui/core/styles';
import Image from 'next/image';

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
		width: '100vw',
		height: '100vh',
		display: 'flex',
		justifyContent: 'center',
		alignItems: 'center'
	},
	container: {
		height: '70vh',
		justifyContent: 'center',
		alignItems: 'center',
		textAlign: 'center'
	}
}));

export default ComingSoon;
