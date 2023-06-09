import { useState, useEffect } from "react";
import { Table, Typography} from 'antd';
import { axiosInstance } from "../../models/axiosInstance";



export const Employees = () => {
  const columns = [
    {
      title: "Email",
      dataIndex: "email",
      key: "email"
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
    axiosInstance.get("/employees/").then(res => setData(res.data));
  }, []);

  return (
    <Table
      columns={columns}
      dataSource={data}
    />
  )
};
