import VerticalLine from '../atoms/VerticalLine'
import styles from '../../styles/BubbleLine.module.css'

export default function BubblesLine({
	children
}: {
	children: React.ReactNode;
}) {
  return (
    <div className={styles.container} >
      {children}
      <VerticalLine />
    </div>
  )
}