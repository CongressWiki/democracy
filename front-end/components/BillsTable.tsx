import React, { Fragment, useEffect, useState } from "react";
import { useApolloClient, useSubscription } from "@apollo/react-hooks";

import DataTable from 'react-data-table-component';
import gql from "graphql-tag";
import moment from 'moment'
import styles from '../styles/Bills.module.css'

const columns = [
  {
    name: 'Subject',
    selector: 'subjects_top_term',
    sortable: true,
    wrap: true,
  },
  {
    name: 'Title',
    selector: 'official_title',
    sortable: true,
    grow: 3,
    wrap: true
  },
  {
    name: 'Status',
    selector: 'actions',
    sortable: true,
    wrap: true,
    cell: row => <div><p>{row.actions[row.actions.length - 1]?.text}</p></div>
  },
  {
    name: 'Updated at',
    selector: 'updated_at',
    sortable: true,
    wrap: true,
    format: row => moment(row.date).format('ll')
  }
];

const customStyles = {
  table: {
    style: {
      height: '100%'
    }
  },
  rows: {
    style: {
      minHeight: '72px', // override the row height
    }
  },
  headCells: {
    style: {
      paddingLeft: '8px', // override the cell padding for head cells
      paddingRight: '8px',
    },
  },
  cells: {
    style: {
      paddingLeft: '8px', // override the cell padding for data cells
      paddingRight: '8px',
      minHeight: '122px',
    },
  },
};

const ExpandableComponent = ({ data }) => <div><p>{data.summary.text}</p></div>;

const Table = props => {
  const [state, setState] = useState({
    proposals: []
  });

  const onRowClicked = (props) => {
    console.log(props)
  }

  useEffect(
    () => {
        setState(prevState => {
          return { ...prevState, proposals: props.proposals };
        });
    },
    []
  );

  return (
    <Fragment>
      <DataTable
        // title="Bills"
        columns={columns}
        data={state.proposals}
        dense
        pagination
        highlightOnHover
        onRowClicked={onRowClicked}
        customStyles={customStyles}
        paginationPerPage={10}
        overflowY
        expandableRows
        expandOnRowClicked
        expandableRowsComponent={<ExpandableComponent />}
        // noTableHead
        />
    </Fragment>
  );
};

// Run a subscription to get the latest Proposal
const GET_LATEST_BILLS = gql`
  subscription getLatestBills {
    bills(
      limit: 50
      order_by: { updated_at: desc }
    ) {
      id
      introduced_at
      official_title
      popular_title
      short_title
      sponsor
      status
      status_at
      subjects
      subjects_top_term
      summary
      titles
      updated_at
      history
      enacted_as
      cosponsors
      committees
      committee_reports
      amendments
      actions
    }
  }
`;

const BillsTable = () => {
  const { loading, error, data } = useSubscription(GET_LATEST_BILLS);
  if (loading) {
    return <span>Loading...</span>;
  }
  if (error) {
    return <span>Error {JSON.stringify(error)}</span>;
  }

  if (data) {
    return (
      <Table proposals={data.bills.length ? data.bills : null} />
    )
  }
};
export default BillsTable;