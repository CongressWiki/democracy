import React from 'react';
import {Grid} from '@material-ui/core';
import {Bill} from '../Bill/Bill';
import type {BillProps} from '../Bill/Bill';

export type BillCanvasProps = {
	bills: BillProps[];
};

const BillCanvas = ({bills}: BillCanvasProps) => {
	return (
		<Grid
			container
			spacing={2}
			direction="column"
		>
			{bills.map(bill => (
				<Grid key={bill.id} item xs>
					<Bill
						id={`${bill.type}.${bill.number}`.toUpperCase()}
						type={bill.type}
						number={bill.number}
						title={bill.title}
						summary={bill.summary}
						actions={bill.actions}
						updated_at={new Date(bill.updated_at)}
						sponsor={bill.sponsor}
					/>
				</Grid>
			))}
		</Grid>
	);
};

export default BillCanvas;
