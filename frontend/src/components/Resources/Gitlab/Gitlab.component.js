import { useState, useEffect } from "react";
import { Space, Switch, Table, Typography} from 'antd';
import { axiosInstance } from "../../../models/axiosInstance";


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


  const [data, setData] = useState([]);
  useEffect(() => {
    axiosInstance.get("/providers/gitlab/").then(res => setData(res.data));
  }, []);

  return (
    <Table
      columns={columns}
      dataSource={data}
      title={() => "Gitlab resources"}
    />
  )
};
