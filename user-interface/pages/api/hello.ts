import { NextApiRequest, NextApiResponse } from 'next'

const hello = (_: NextApiRequest, response: NextApiResponse) => {
  response.status(200).json({ text: 'Hello' })
}

export default hello
