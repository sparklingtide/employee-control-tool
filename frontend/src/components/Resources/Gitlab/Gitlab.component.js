import { useState } from "react";
import { Space, Switch, Table, Typography} from 'antd';


export const Gitlab = () => {
  const columns = [
    {
      title: "Name",
      dataIndex: "name",
      key: "name"
    },
    {
      title: "Project",
      dataIndex: "project_id",
      key: "project_id"
    },
    {
      title: "Role",
      dataIndex: "role",
      key: "role"
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
      id: 5,
      name: "Main group",
      project_id: "1123554",
      role: "developer"
    },
    {
      id: 6,
      name: "Samolet dev",
      project_id: "448784",
      role: "guest"
    }
  ]
  return (
    <Table
      columns={columns}
      dataSource={data}
      title={() => "Gitlab resources"}
    />
  )
};
