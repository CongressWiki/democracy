import { Bill, BillProps } from "../components/Bill/Bill";
// Also exported from '@storybook/react' if you can deal with breaking changes in 6.1
import { Meta, Story } from "@storybook/react/types-6-0";

import React from "react";

export default {
  title: "Example/Bill",
  component: Bill,
} as Meta;

const Template: Story<BillProps> = (args) => <Bill {...args} />;

export const Default = Template.bind({});
Default.args = {
  id: "id",
  title: "Title",
  summary: "Summary",
};

export const ExampleA = Template.bind({});
ExampleA.args = {
  id: "H.R.1234",
  title:
    "To amend the Controlled Substances Act to clarify the process for registrants to exercise due diligence upon discovering a suspicious order, and for other purposes.",
  summary:
    "Block, Report, And Suspend Suspicious Shipments Act of 2020\n\nThis bill creates additional requirements for drug manufacturers and distributors who discover a suspicious order for controlled substances.\n\nIn addition to reporting the suspicious order to the Drug Enforcement Administration, a manufacturer or distributor must also exercise due diligence and decline to fill the order.",
};

export const Skeleton = Template.bind({});
Skeleton.args = {
  id: null,
  title: null,
  summary: null,
};
