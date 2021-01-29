import {Bill} from '../Bill/Bill';
import {makeStyles} from '@material-ui/core/styles';
import React from 'react';
import Grid from '@material-ui/core/Grid';
import type {BillProps} from '../Bill/Bill';

export type BillCanvasProps = {
	bills: BillProps[];
};

const BillCanvas = ({bills}: BillCanvasProps) => {
	const classes = useStyles();
	return (
		<div className={classes.root}>
			<Grid
				container
				spacing={3}
				className={classes.billRow}
				direction="column"
			>
				{bills.map(bill => (
					<Grid key={bill.id} item xs className={classes.bill}>
						<Bill
							id={`${bill.type}.${bill.number}`.toUpperCase()}
							title={bill?.title}
							summary={bill?.summary}
							actions={bill?.actions}
							updated_at={new Date(bill?.updated_at)}
							sponsor={bill?.sponsor}
						/>
					</Grid>
				))}
			</Grid>
		</div>
	);
};

const useStyles = makeStyles(() => ({
	root: {
		flexGrow: 1
	},
	billRow: {},
	bill: {
		alignSelf: 'center'
	}
}));

export default BillCanvas;
