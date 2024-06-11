#include <iostream>
#include <cstddef>
#include <stack>

class Foo {
    public:
        Foo(int x, double y): m_x{x}, m_y{y} {}
        void bar() const
        {
            std::cout << m_x << ", " << m_y << std::endl;
        }
    private:
        int m_x;
        double m_y;
};

template <typename T, std::size_t kSize>
class StaticAllocator
{
    public:
        template <class... Args>
        T* New(Args&&... args)
        {
            T* elem;
            if (N == kSize)
            {
                if (m_pointers.empty())
                {
                    return nullptr;
                }

                elem = m_pointers.top();
                m_pointers.pop();
            }
            else
            {
                elem = reinterpret_cast<T*>(&m_storage[N * sizeof(T)]);
                ++N;
            }
            new (elem) T(std::forward<Args>(args)...);
            ++m_size;
            return elem;
        }

        void Delete(T* t)
        {
            if (t)
            {
                m_pointers.push(t);
                t->~T();
                --m_size;
            }
        }

    private:
        std::byte m_storage[kSize];
        std::stack<T*> m_pointers;
        std::size_t N{};
        std::size_t m_size{};
};


int main()
{
    StaticAllocator<Foo, 2> sa;

    Foo* f1 = sa.New(10, 2.3);
    Foo* f2 = sa.New(20, 5.8);
    Foo* f3 = sa.New(30, 0.6); // f3 = nullptr

    f1->bar();
    f2->bar();

    sa.Delete(f1);
    sa.Delete(f2);
    sa.Delete(f3); // delete for nullptr works fin

    return 0;
}



