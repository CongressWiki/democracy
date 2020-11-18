import React, { Fragment, useEffect, useState } from "react";
import { useApolloClient, useSubscription } from "@apollo/react-hooks";

import DataTable from 'react-data-table-component';
import gql from "graphql-tag";
import moment from 'moment'

const columns = [
  {
    name: 'Category',
    selector: 'category',
    sortable: true,
    wrap: true,
    format: row => row.category.charAt(0).toUpperCase() + row.category.slice(1)
  },
  {
    name: 'Question',
    selector: 'question',
    sortable: true,
    grow: 3,
    wrap: true
  },
  {
    name: 'Result',
    selector: 'result',
    sortable: true,
    wrap: true
  },
  {
    name: 'Date',
    selector: 'date',
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
        title="Senate Proposals"
        columns={columns}
        data={state.proposals}
        dense
        pagination
        highlightOnHover
        onRowClicked={onRowClicked}
        customStyles={customStyles}
        paginationPerPage={3}
        overflowY
        />
    </Fragment>
  );
};

// Run a subscription to get the latest Proposal
const GET_LATEST_PROPOSALS = gql`
  subscription getLatestProposals {
    proposals(
      limit: 50
      order_by: { date: desc }
    ) {
      id
      category
      type
      question
      subject
      created_at
      result
      source_url
      date
    }
  }
`;

const ProposalsTable = () => {
  const { loading, error, data } = useSubscription(GET_LATEST_PROPOSALS);
  if (loading) {
    return <span>Loading...</span>;
  }
  if (error) {
    return <span>Error {JSON.stringify(error)}</span>;
  }

  if (data) {
    return (
      <Table proposals={data.proposals.length ? data.proposals : null} />
    )
  }
};
export default ProposalsTable;