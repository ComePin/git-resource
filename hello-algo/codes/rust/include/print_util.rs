/*
 * File: print_util.rs
 * Created Time: 2023-02-05
 * Author: sjinzh (sjinzh@gmail.com), xBLACKICEx (xBLACKICEx@outlook.com)
 */

use std::cell::{Cell, RefCell};
use std::fmt::Display;
use std::collections::{HashMap, VecDeque};
use std::rc::Rc;

use crate::list_node::ListNode;
use crate::tree_node::{TreeNode, vec_to_tree};

struct Trunk<'a, 'b> {
    prev: Option<&'a Trunk<'a, 'b>>,
    str: Cell<&'b str>,
}

/* Print an array */
pub fn print_array<T: Display>(nums: &[T]) {
    print!("[");
    if nums.len() > 0 {
        for (i, num) in nums.iter().enumerate() {
            print!("{}{}", num, if i == nums.len() - 1 {"]"} else {", "} );
        }
    } else {
        print!("]");
    }
}

/* Print a hash map */
pub fn print_hash_map<TKey: Display, TValue: Display>(map: &HashMap<TKey, TValue>) {
    for (key, value) in map {
        println!("{key} -> {value}");
    }
}

/* Print a queue or deque */
pub fn print_queue<T: Display>(queue: &VecDeque<T>) {
    print!("[");
    let iter = queue.iter();
    for (i, data) in iter.enumerate() {
        print!("{}{}", data, if i == queue.len() - 1 {"]"} else {", "} );
    }
}

/* Print a linked list */
pub fn print_linked_list<T: Display>(head: &Rc<RefCell<ListNode<T>>>) {
    print!("{}{}", head.borrow().val, if head.borrow().next.is_none() {"\n"} else {" -> "});
    if let Some(node) = &head.borrow().next {
        return print_linked_list(node);
    }
}

pub fn print_tree(root: &Rc<RefCell<TreeNode>>) {
    _print_tree(Some(root), None, false);
}

fn _print_tree(root: Option<&Rc<RefCell<TreeNode>>>, prev: Option<&Trunk>, is_left: bool) {
    if let Some(node) = root {
        let mut prev_str = "    ";
        let trunk = Trunk { prev, str: Cell::new(prev_str) };
        _print_tree(node.borrow().right.as_ref(), Some(&trunk), true);

        if  prev.is_none() {
            trunk.str.set("———");
        } else if is_left {
            trunk.str.set("/———");
            prev_str = "   |";
        } else {
            trunk.str.set("\\———");
            prev.as_ref().unwrap().str.set(prev_str);
        }

        show_trunks(Some(&trunk));
        println!(" {}", node.borrow().val);
        if let Some(prev) = prev {
            prev.str.set(prev_str);
        }
        trunk.str.set("   |");

        _print_tree(node.borrow().left.as_ref(), Some(&trunk), false);
    }
}

fn show_trunks(trunk: Option<&Trunk>) {
    if let Some(trunk) = trunk {
        show_trunks(trunk.prev);
        print!("{}", trunk.str.get());
    }
}

/* Print a heap both in array and tree representations */
pub fn print_heap(heap: Vec<i32>) {
    println!("堆的数组表示：{:?}", heap);
    println!("堆的树状表示：");
    if let Some(root) = vec_to_tree(heap.into_iter().map(|val| Some(val)).collect()) {
        print_tree(&root);
    } 
}