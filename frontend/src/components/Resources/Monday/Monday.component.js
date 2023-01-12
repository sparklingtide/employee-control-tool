import { useState } from "react";
import { Space, Switch, Table, Typography} from 'antd';


export const Monday = () => {
  const columns = [
    {
      title: "Name",
      dataIndex: "name",
      key: "name"
    },
    {
      title: "Board",
      dataIndex: "board_id",
      key: "board_id"
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
      id: 3,
      name: "Main group",
      board_id: "1123554"
    },
    {
      id: 4,
      name: "Samolet dev",
      board_id: "554688456"
    }
  ]
  return (
    <Table
      columns={columns}
      dataSource={data}
      title={() => "Monday resources"}
    />
  )
};
