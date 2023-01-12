import { useState } from "react";
import { Space, Switch, Table, Typography} from 'antd';


export const Telegram = () => {
  const columns = [
    {
      title: "Name",
      dataIndex: "name",
      key: "name"
    },
    {
      title: "Telegram group",
      dataIndex: "group_id",
      key: "group_id"
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
      name: "Main group",
      group_id: "1123554"
    },
    {
      id: 2,
      name: "Samolet dev",
      group_id: "554688456"
    }
  ]
  return (
    <Table
      columns={columns}
      dataSource={data}
      title={() => "Telegram resources"}
    />
  )
};
