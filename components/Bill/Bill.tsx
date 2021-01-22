import { makeStyles, useTheme } from "@material-ui/core/styles";

import Divider from "@material-ui/core/Divider";
import Grid from "@material-ui/core/Grid";
import Paper from "@material-ui/core/Paper";
import PropTypes from "prop-types";
import React from "react";
import Skeleton from "@material-ui/lab/Skeleton";
import Typography from "@material-ui/core/Typography";

export interface BillProps {
  /**
   * Bill ID
   */
  id: string;

  /**
   * Bill title
   */
  title: string;

  /**
   * Summary of bill
   */
  summary: string;
}

const useStyles = makeStyles((theme) => ({
  paper: {
    flexGrow: 1,
    width: "calc((8.5/14) * .5 * 100vw)",
    // aspectRatio: "1 / 1.6471",
    height: "calc((14/8.5) * .5 * 100vh)",
    margin: theme.spacing(4),
    // marginLeft: theme.spacing(2),
    borderRadius: 1,
    padding: theme.spacing(4),
    background: "rgba(224, 211, 175)",
    boxShadow: "0 3px 5px 2px rgba(0, 0, 0, .1)",
  },
  id: {
    margin: "auto",
  },
  indent: (props) => ({
    // TextIndent: "-3em",
    // paddingLeft: "3em",
  }),
  divider: {
    // MarginTop: theme.spacing(2),
    // marginBottom: theme.spacing(2),
    backgroundColor: "black",
    // Height: 1,
    // Width: '60%'
  },
}));

export const Bill = (props) => {
  const classes = useStyles();

  return (
    <Paper elevation={3} className={classes.paper}>
      <Grid container direction="column" spacing={1}>
        {/* ID */}
        <Grid item xs className={classes.id}>
          {props.id ? (
            <Typography>{props.id}</Typography>
          ) : (
            <Skeleton
              variant="text"
              animation="wave"
              // Height={22}
              // width="10%"
              // style={{ marginBottom: theme.spacing(4) }}
            />
          )}
        </Grid>
        {/* Title */}
        <Grid item xs>
          {props.title ? (
            <Typography className={classes.indent}>{props.title}</Typography>
          ) : (
            <Skeleton
              variant="text"
              animation="wave"
              // Height={22}
              // width="80%"
              // style={{ marginBottom: theme.spacing(4) }}
            />
          )}
        </Grid>
        {/* Divider */}
        {/* <Grid item xs>
          <Divider variant="fullWidth" className={classes.divider} />
        </Grid> */}
        {/* Summary */}
        {/* <Grid item xs>
          {props.summary ? (
            <Typography className={classes.indent}>{props.summary}</Typography>
          ) : (
            <Skeleton
              variant="text"
              animation="wave"
              // height={18}
            />
          )}
        </Grid> */}
      </Grid>
    </Paper>
  );
};

Bill.propTypes = {
  id: PropTypes.string,
  title: PropTypes.string,
  summary: PropTypes.string,
};
