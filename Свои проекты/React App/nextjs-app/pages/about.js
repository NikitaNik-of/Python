import Link from "next/link";
import Head from 'next/head'
import Layout from "../components/Layout";
import ActBtn from "../components/UI/ActBtn";
import InactBtn from "../components/UI/InactBtn";
import { useState } from "react";


export default function About() {
    
    const [curPage, setCurPage] = useState('/about')
    const [navPages, setNavPages] = useState([
        {id: 1, name: 'Главная страница', adress: '/'},
        {id: 2, name: 'О сайте', adress: '/about'}]
    );

    return(
    <>
        <nav className=' backdrop-blur top-0 z-40 sticky bg-white/70 border-b border-gray-400'>
            <div className=' w-4/5 mx-auto'>
                <div className='flex space-x-4 py-3 items-center'>
                    {navPages.map((pages) => (
                        <Link href={pages.adress} passHref>
                            {(curPage == pages.adress)
                                ? <ActBtn onClick={() => setCurPage(pages.adress)}>{pages.name}</ActBtn>
                                : <InactBtn onClick={() => setCurPage(pages.adress)}>{pages.name}</InactBtn>}
                        </Link>
                    ))}
                </div>
            </div>
        </nav>

        <Layout>
            <Head>
                <title>О сайте</title>
            </Head>
            <h1 className=" text-6xl mb-3">This is about page</h1>
            <h2 className=" text-2xl"><Link href='/'>okay, let me back!</Link></h2>
            <h1 className=" text-6xl mb-3">This is about page</h1>
            <h2 className=" text-2xl"><Link href='/'>okay, let me back!</Link></h2>
            <h1 className=" text-6xl mb-3">This is about page</h1>
            <h2 className=" text-2xl"><Link href='/'>okay, let me back!</Link></h2>
            <h1 className=" text-6xl mb-3">This is about page</h1>
            <h2 className=" text-2xl"><Link href='/'>okay, let me back!</Link></h2>
            <h1 className=" text-6xl mb-3">This is about page</h1>
            <h2 className=" text-2xl"><Link href='/'>okay, let me back!</Link></h2>
            <h1 className=" text-6xl mb-3">This is about page</h1>
            <h2 className=" text-2xl"><Link href='/'>okay, let me back!</Link></h2>
            <h1 className=" text-6xl mb-3">This is about page</h1>
            <h2 className=" text-2xl"><Link href='/'>okay, let me back!</Link></h2>
            <h1 className=" text-6xl mb-3">This is about page</h1>
            <h2 className=" text-2xl"><Link href='/'>okay, let me back!</Link></h2>
            <h1 className=" text-6xl mb-3">This is about page</h1>
            <h2 className=" text-2xl"><Link href='/'>okay, let me back!</Link></h2>
            <h1 className=" text-6xl mb-3">This is about page</h1>
            <h2 className=" text-2xl"><Link href='/'>okay, let me back!</Link></h2>
            <h1 className=" text-6xl mb-3">This is about page</h1>
            <h2 className=" text-2xl"><Link href='/'>okay, let me back!</Link></h2>
        </Layout>
    </>
    )
}