import { Bill } from "./Bill/Bill";
import CircularProgress from "@material-ui/core/CircularProgress";
import { makeStyles } from "@material-ui/core/styles";
import React from "react";
import gql from "graphql-tag";
import { useQuery } from "@apollo/react-hooks";
import Grid from "@material-ui/core/Grid";

const GET_LATEST_BILLS = gql`
  query getLatestBills {
    bills(limit: 3, order_by: { status_at: desc }) {
      id
      type
      number
      by_request
      subject
      introduced_at
      updated_at
      title
      summary
      status
      status_at
      congress
      actions
      sponsor
    }
  }
`;

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  billRow: {
    backgroundColor: "red",
  },
  bill: {
    alignSelf: "center",
  },
}));

const BillCanvas = () => {
  const { loading, error, data } = useQuery(GET_LATEST_BILLS);
  const classes = useStyles();

  if (loading) {
    return <CircularProgress />;
  }

  if (error) {
    return <span>Error {JSON.stringify(error, null, 2)}</span>;
  }

  if (data.bills) {
    return (
      <div className={classes.root}>
        <Grid
          container
          spacing={3}
          className={classes.billRow}
          direction="column"
        >
          {data.bills.map((billData) => (
            <Grid item className={classes.bill}>
              <Bill
                id={`${billData.type}.${billData.number}`.toUpperCase()}
                title={billData?.title}
                summary={billData?.summary}
              />
            </Grid>
          ))}
        </Grid>
      </div>
    );
  }
};

export default BillCanvas;
