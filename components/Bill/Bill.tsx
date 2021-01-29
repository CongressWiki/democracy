import { makeStyles } from "@material-ui/core/styles";

import Grid from "@material-ui/core/Grid";
import Card from "@material-ui/core/Card";
import React from "react";
import Skeleton from "@material-ui/lab/Skeleton";
import Typography from "@material-ui/core/Typography";
import Avatar from "@material-ui/core/Avatar";
import Image from "next/image";
import { Tooltip } from "@material-ui/core";

// import Stepper from "@material-ui/core/Stepper";
// import Step from "@material-ui/core/Step";
// import StepLabel from "@material-ui/core/StepLabel";

export type BillProps = {
  id: string;
  type: string;
  number: string;
  title: string;
  summary: string;
  actions: Array<Record<string, any>>;
  updated_at: Date;
  sponsor: string;
};

export const Bill = (props) => {
  const classes = useStyles();
  const updated_at = new Date(props.updated_at).toDateString();

  return (
    <Card elevation={3} className={classes.root}>
      <Grid container spacing={1}>
        <Grid container justify="space-between">
          <Grid item xs={4} />
          {/* ID */}
          <Grid item xs={4}>
            {props.id ? (
              <Typography variant="h6" align="center">
                {props.id}
              </Typography>
            ) : (
              <Skeleton
                variant="text"
                animation="wave"
                height={22}
                width="30%"
              />
            )}
          </Grid>
          {/* Date */}
          <Grid item xs={4}>
            {props.updated_at ? (
              <Typography display="block" align="right" variant="caption">
                {updated_at}
              </Typography>
            ) : (
              <Skeleton
                variant="text"
                animation="wave"
                height={22}
                width="30%"
              />
            )}
          </Grid>
        </Grid>

        {/* Title */}
        <Grid item xs={12}>
          {props.title ? (
            <Typography className={classes.title} variant="body1" paragraph>
              {props.title}
            </Typography>
          ) : (
            <Skeleton variant="text" animation="wave" height={22} width="80%" />
          )}
        </Grid>

        {/* Stepper */}
        {/* <Stepper activeStep={props.actions.length - 1} alternativeLabel>
          {props.actions.map((action, index) => (
            <Step key={index}>
              <StepLabel>{action.text.slice(0, 60) + "..."}</StepLabel>
            </Step>
          ))}
        </Stepper> */}

        {/* Sponsor image */}
        <Grid item xs={4} />
        <Grid item xs={4} container justify="center">
          <Tooltip title="Sponsor">
            <Avatar className={classes.sponsorAvatar}>
              <Image
                src={`/elected_official_images/congress/original/${props.sponsor}.jpg`}
                layout="fill"
                objectFit="cover"
                objectPosition="50% 20%"
                quality={100}
              />
            </Avatar>
          </Tooltip>
        </Grid>
        <Grid item xs={4} />
      </Grid>
    </Card>
  );
};

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
    maxWidth: "600px",
    borderRadius: 5,
    padding: theme.spacing(2),
    border: "0.2em solid #edccab",
    boxShadow: "0 3px 5px 2px rgba(0, 0, 0, .1)",
    overflow: "hidden",
  },
  // indent: (props) => ({
  // TextIndent: "-3em",
  // paddingLeft: "3em",
  // }),
  sponsorAvatar: {
    width: theme.spacing(7),
    height: theme.spacing(7),
  },
  title: {
    paddingLeft: theme.spacing(3),
    paddingRight: theme.spacing(3),
  },
}));
