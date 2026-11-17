// conv <in> <out>: converts between binary (.rbxm/.rbxl) and XML (.rbxmx/.rbxlx) by extension.
use std::{env, fs::File, io::{BufReader, BufWriter}};
fn main() {
    let a: Vec<String> = env::args().collect();
    let r = BufReader::new(File::open(&a[1]).unwrap());
    let dom = if a[1].ends_with('x') {
        rbx_xml::from_reader_default(r).expect("read xml")
    } else {
        rbx_binary::from_reader(r).expect("read binary")
    };
    let roots = dom.root().children().to_vec();
    let w = BufWriter::new(File::create(&a[2]).unwrap());
    if a[2].ends_with('x') {
        rbx_xml::to_writer_default(w, &dom, &roots).expect("write xml");
    } else {
        rbx_binary::to_writer(w, &dom, &roots).expect("write binary");
    }
    println!("{} -> {} ({} root instances)", a[1], a[2], roots.len());
}
