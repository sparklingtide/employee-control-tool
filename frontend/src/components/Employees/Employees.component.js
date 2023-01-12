import { useState } from "react";
import { Space, Switch, Table, Typography} from 'antd';


export const Employees = () => {
  const columns = [
    {
      title: "Name",
      dataIndex: "name",
      key: "name"
    },
    {
      title: "Actions",
      dataIndex: "",
      width: "20%",
      render: (_, record) => (
        <span>
          <Typography.Link
            style={{
              marginRight: 8
            }}
          >
            Edit
          </Typography.Link>

          <Typography.Link>
            Delete
          </Typography.Link>
        </span>
      )
    }
  ]

  const data = [
    {
      id: 1,
      name: "Root",
    },
    {
      id: 2,
      name: "Test"
    }
  ]
  return (
    <Table
      columns={columns}
      dataSource={data}
    />
  )
};
