import Link from "next/link";
import Head from "next/head";
import Layout from "../components/Layout";
import Image from 'next/image'
import { useRouter } from "next/router";
import NavBar from "../components/NavBar";
import MainButton from "../components/UI/MainButton";

export default function Home() {
  return (
    <div>
      <NavBar/>
      <Layout>
        <Head>
          <title>Главная страница</title>
        </Head>
        <div className='flex flex-col justify-center text-center items-center my-32'>
          <h1 className="flex items-center transition-colors text-6xl font-bold mb-6">Привет!
            <span className="ml-8 ">
              <Image src={'/images/wave.png'} height={90} width={90} layout="fixed" onBlur={true}/>
            </span>
          </h1>
          <h2 className=" transition-colors text-3xl my-2">{'Добро пожаловать на '}
            <span className=" transition-colors bg-gradient-to-br from-emerald-500 via-cyan-500 to-indigo-500 text-transparent bg-clip-text">
              мой сайт!
            </span>
          </h2>
        </div>
        <div className="space-x-4">
          <MainButton>LULE</MainButton>
          <MainButton>LULE</MainButton>
          <MainButton>LULE</MainButton>
          <MainButton>LULE</MainButton>
          <MainButton>LULE</MainButton>
          <MainButton>LULE</MainButton>
          <MainButton>LULE</MainButton>
          <MainButton>LULE</MainButton>
          <MainButton>LULE</MainButton>
        </div>
      </Layout>
    </div>
  );
}
