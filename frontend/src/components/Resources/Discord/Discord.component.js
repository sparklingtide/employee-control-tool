import { useState } from "react";
import { Space, Switch, Table, Typography} from 'antd';


export const Discord = () => {
  const columns = [
    {
      title: "Name",
      dataIndex: "name",
      key: "name"
    },
    {
      title: "Server",
      dataIndex: "server_id",
      key: "server_id"
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
      id: 7,
      name: "Main group",
      servier_id: "1123554",
    },
    {
      id: 8,
      name: "Samolet dev",
      server_id: "448784",
    }
  ]
  return (
    <Table
      columns={columns}
      dataSource={data}
      title={() => "Discord resources"}
    />
  )
};
