import {Bill, BillProps} from '../components/Bill';
// Also exported from '@storybook/react' if you can deal with breaking changes in 6.1
import {Meta, Story} from '@storybook/react/types-6-0';

import React from 'react';

export default {
	title: 'Example/Bill',
	component: Bill,
	argTypes: {
		backgroundColor: {control: 'color'}
	}
} as Meta;

const Template: Story<BillProps> = args => <Bill {...args}/>;

export const Primary = Template.bind({});
Primary.args = {
	subjects_top_term: 'Health',
	official_title: 'Title',
	summary: 'summary'
};
